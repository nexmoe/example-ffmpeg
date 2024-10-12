<script setup>
import HelloWorld from './components/HelloWorld.vue'
import { ref } from 'vue'
const file = ref(null)
const video = ref()
const downloada = ref()
const loading = ref(false)
const videoUrl = ref()

async function uploadVideo(event) {
	file.value = event.target.files[0]
	if (!file.value) return

	const formData = new FormData()
	formData.append('file', file.value)

	try {
		loading.value = true
		const response = await fetch('/video/to/mp4', {
			method: 'POST',
			body: formData,
		})

		if (!response.ok) {
			throw new Error(`HTTP error! Status: ${response.status}`)
		}

		const blob = await response.blob()
		const url = URL.createObjectURL(blob)

		videoUrl.value = url
    	loading.value = false
	} catch (error) {
		console.error('Error:', error)
	}
}
</script>

<template>
	<div class="min-h-screen bg-gray-100 flex items-center justify-center">
		<div class="container mx-auto px-4">
			<div class="w-full grid md:grid-cols-2 gap-6 py-8">
				<div class="bg-white rounded-lg p-6 border border-input shadow-sm">
					<div class="flex flex-col items-center justify-center h-full">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							class="w-12 h-12 text-primary"
						>
							<path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"></path>
							<path d="M12 12v9"></path>
							<path d="m16 16-4-4-4 4"></path>
						</svg>
						<h3 class="text-xl font-semibold mt-4">上传视频</h3>
						<p class="text-muted-foreground text-sm mt-2">
							点击上传视频按钮上传任意格式视频，转化为 MP4
						</p>
						<input id="dropzone-file" @change="uploadVideo" type="file" class="hidden" />
						<label
							v-if="!loading"
							for="dropzone-file"
							class="cursor-pointer text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
						>
							选择视频
						</label>

						<button
							v-else
							disabled
							type="button"
							class="text-white bg-gray-800 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 inline-flex items-center"
						>
							<svg
								aria-hidden="true"
								role="status"
								class="inline w-4 h-4 me-3 text-white animate-spin"
								viewBox="0 0 100 101"
								fill="none"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
									fill="#E5E7EB"
								/>
								<path
									d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
									fill="currentColor"
								/>
							</svg>
							上传中...
						</button>
					</div>
				</div>
				<div class="bg-white rounded-lg p-6 border border-input shadow-sm">
					<div
						v-if="loading"
						class="flex items-center justify-center bg-gray-100 opacity-50 absolute w-full h-full left-0 top-0 z-100"
					>
						<svg
							aria-hidden="true"
							role="status"
							class="inline w-12 h-12 me-3 text-black animate-spin"
							viewBox="0 0 100 101"
							fill="none"
							xmlns="http://www.w3.org/2000/svg"
						>
							<path
								d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
								fill="#E5E7EB"
							/>
							<path
								d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
								fill="currentColor"
							/>
						</svg>
					</div>
					<div class="flex flex-col gap-4">
						<div class="flex items-center justify-between">
							<div>
								<h4 class="my-0 text-lg font-semibold">视频预览</h4>
							</div>
							<div class="flex gap-2">
								<a
									v-if="videoUrl"
									ref="downloada"
									:href="videoUrl"
									class="decoration-none text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700 flex items-center"
									download
								>
									<svg
										xmlns="http://www.w3.org/2000/svg"
										width="24"
										height="24"
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2"
										stroke-linecap="round"
										stroke-linejoin="round"
										class="w-4 h-4 mr-2"
									>
										<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
										<polyline points="7 10 12 15 17 10"></polyline>
										<line x1="12" x2="12" y1="15" y2="3"></line>
									</svg>
									下载视频
								</a>
							</div>
						</div>
						<div class="aspect-video rounded-lg overflow-hidden">
							<video
								v-if="videoUrl"
								:src="videoUrl"
								class="w-full h-full"
								ref="video"
								controls
							></video>
							<div
								class="w-full h-full bg-gray-100 rounded-lg flex items-center justify-center"
								v-else
							>
								请先上传视频
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
