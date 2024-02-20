import { createBrowserRouter } from "react-router-dom";
import { AppLayout } from "../layout/AppLayout.js";
import { RootError } from "../layout/RootError.js";

/**
 * Application routes
 * https://reactrouter.com/en/main/routers/create-browser-router
 */
export const router = createBrowserRouter([
  {
    path: "",
    element: <AppLayout />,
    errorElement: <RootError />,
    children: [
      // { index: true, element: <Navigate to="/list" replace /> },
      {
        path: "",
        lazy: () => import("../pages/index.js"),
      },
      {
        path: "dashboard",
        lazy: () => import("../pages/dashboard/Dashboard.js"),
      },
    ],
  },
]);

// Clean up on module reload (HMR)
// https://vitejs.dev/guide/api-hmr
if (import.meta.hot) {
  import.meta.hot.dispose(() => router.dispose());
}
