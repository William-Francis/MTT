import { Box, GlobalStyles } from "@mui/joy";
import * as React from "react";
import { Outlet } from "react-router-dom";
import { BaseToolbar } from "./components/BaseToolbar.js";

/**
 * The minimal app layout to be used on pages such Login/Signup,
 * Privacy Policy, Terms of Use, etc.
 */
export function BaseLayout(): JSX.Element {
  return (
    <>
      <GlobalStyles
        styles={{
          "#root": {
            display: "flex",
            flexDirection: "column",
            minHeight: "100vh",
          },
        }}
      />

      <BaseToolbar />
      <Box sx={{ display: "flex", minHeight: "100dvh" }}>
        <Box
          component="main"
          className="MainContent"
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
