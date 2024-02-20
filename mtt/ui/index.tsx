import CssBaseline from "@mui/joy/CssBaseline";
import { CssVarsProvider } from "@mui/joy/styles";
import {
  DefaultOptions,
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query";
import * as React from "react";
import * as ReactDOM from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import "./assets/styles/index.tsx";
import { router } from "./routes/index.js";
const container = document.getElementById("root") as HTMLElement;
const root = ReactDOM.createRoot(container);

export const defaultOptions: DefaultOptions<unknown> = {
  queries: {
    retry: false,
    refetchOnWindowFocus: false,
    keepPreviousData: false,
    suspense: true,
    staleTime: 2000,
  },
};
const queryClient = new QueryClient({ defaultOptions });
// Render the top-level React component
root.render(
  <React.StrictMode>
    <CssVarsProvider disableTransitionOnChange>
      <CssBaseline />
      <QueryClientProvider client={queryClient}>
        <RouterProvider router={router} />
        {/* <ReactQueryDevtools initialIsOpen={false} /> */}
      </QueryClientProvider>
    </CssVarsProvider>
  </React.StrictMode>
);
