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
		adapter: adapter(),
		alias: {
			$api: './src/api',
			$assets: './src/assets',
			$components: './src/components',
			$config: './src/config',
			$constants: './src/constants',
			$controllers: './src/controllers',
			$directives: './src/directives',
			$generated: './src/generated',
			$graphql: './src/graphql',
			$hooks: './src/hooks',
			$layouts: './src/routes/layouts',
			$lib: './src/lib',
			$middlewares: './src/middlewares',
			$pages: './src/routes/pages',
			$repositories: './src/repositories',
			$routes: './src/routes',
			$services: './src/services',
			$src: './src',
			$stores: './src/stores',
			$styles: './src/styles',
			$types: './src/types',
			$utils: './src/utils',
			$validators: './src/validators'
		}
	}
};

export default config;
