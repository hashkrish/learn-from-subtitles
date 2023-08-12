import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		// adapter-auto only supports some environments, see https://kit.svelte.dev/docs/adapter-auto for a list.
		// If your environment is not supported or you settled on a specific environment, switch out the adapter.
		// See https://kit.svelte.dev/docs/adapters for more information about adapters.
		adapter: adapter()
	},
	alias: {
		$components: './src/components',
		$stores: './src/stores',
		$utils: './src/utils',
		$styles: './src/styles',
		$assets: './src/assets',
		$routes: './src/routes',
		$layouts: './src/routes/layouts',
		$pages: './src/routes/pages',
		$services: './src/services',
		$types: './src/types',
		$config: './src/config',
		$hooks: './src/hooks',
		$constants: './src/constants',
		$api: './src/api',
		$graphql: './src/graphql',
		$generated: './src/generated',
		$directives: './src/directives',
		$middlewares: './src/middlewares',
		$validators: './src/validators',
		$repositories: './src/repositories',
		$controllers: './src/controllers'
	}
};

export default config;
