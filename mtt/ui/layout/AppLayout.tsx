import { Box } from "@mui/joy";
import * as React from "react";
import { Outlet } from "react-router-dom";
import { AppToolbar } from "./components/AppToolbar.js";

/**
 * The primary application layout.
 */
export function AppLayout(): JSX.Element {
  return (
    <>
      <AppToolbar />
      <Box sx={{ display: "flex", minHeight: "100dvh" }}>
        <Box
          component="main"
          className="MainContent"
          style={{ paddingTop: 0 }}
          sx={{
            px: {
              xs: 2,
              md: 6,
            },
            pt: {
              xs: "calc(12px + var(--Header-height))",
              sm: "calc(12px + var(--Header-height))",
              md: 3,
            },
            pb: {
              xs: 2,
              sm: 2,
              md: 3,
            },
            flex: 1,
            display: "flex",
            flexDirection: "column",
            minWidth: 0,
            height: "100dvh",
            gap: 1,
          }}
        >
          <React.Suspense>
            <Outlet />
          </React.Suspense>
        </Box>
      </Box>
    </>
  );
}
