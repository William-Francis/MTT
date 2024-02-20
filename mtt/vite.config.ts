import react from "@vitejs/plugin-react";
import path from "path";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => ({
  plugins: [react(), tsconfigPaths()],
  server: {
    // need origin for static image in dev https://github.com/MrBin99/django-vite/issues/7
    origin: "http://localhost:3000",
    host: "localhost",
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  root: path.resolve("./ui"),
  base: "/static/",
  build: {
    outDir: path.resolve("./static/dist"),
    manifest: true,
    rollupOptions: {
      input: {
        main: path.resolve("./ui/index.tsx"),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
    define: {
      __DEV__: JSON.stringify(mode !== "production"),
    },
  },
}));
