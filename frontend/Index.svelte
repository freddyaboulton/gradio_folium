<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block, BlockLabel } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { onDestroy } from "svelte";
	import type { FileData } from "@gradio/client";
	import { Empty } from "@gradio/atoms";
	import { Plot as PlotIcon } from "@gradio/icons";

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: FileData;
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let root: string;
	export let root_url: string;
	export let height: number = 500;
	export let gradio: Gradio<{
		change: never;
	}>;

	let new_value: FileData;
	let blobUrl: string | null = null;

	async function createBlobUrl() {
		if (blobUrl) {
			URL.revokeObjectURL(blobUrl);
		}

		if (new_value?.url) {
			try {
				const response = await fetch(new_value.url);
				const html = await response.text();
				const blob = new Blob([html], { type: 'text/html' });
				blobUrl = URL.createObjectURL(blob);
			} catch (error) {
				console.error('Error creating blob URL:', error);
			}
		}
	}

	async function handle_change() {
		await createBlobUrl();
		gradio.dispatch("change");
	}

	onDestroy(() => {
		if (blobUrl) {
			URL.revokeObjectURL(blobUrl);
		}
	});

	$: height = height ?? 500;
	$: label = label ?? "Folium Map";
	$: new_value = {...value};
	$: new_value, handle_change();
</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
	{#if loading_status}
		<StatusTracker
			autoscroll={gradio.autoscroll}
			i18n={gradio.i18n}
			{...loading_status}
		/>
	{/if}
	<BlockLabel show_label={true} Icon={PlotIcon} {label} />
	{#if value}
		<iframe 
			src={blobUrl} 
			title={label} 
			height="{height}px"
			sandbox="allow-same-origin allow-scripts"
		></iframe>
	{:else}
		<Empty unpadded_box={true} size="large"><PlotIcon /></Empty>
	{/if}
</Block>

<style>
	iframe {
		display: flex;
		width: var(--size-full);
		border: none;
	}
</style>