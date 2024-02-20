import { Box } from "@mui/joy";
import { Outlet } from "react-router-dom";

export function Component(): JSX.Element {
  return (
    <Box>
      <Outlet />
    </Box>
  );
}

Component.displayName = "SettingsLayout";
