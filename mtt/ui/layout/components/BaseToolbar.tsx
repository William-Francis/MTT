import { Box, IconButton } from "@mui/joy";
import { FaCross } from "react-icons/fa";
import { Link } from "../../common/Link.js";
import { Logo } from "./Logo.js";

export function BaseToolbar(props: any): JSX.Element {
  return (
    <div color="transparent" elevation={0} {...props}>
      <div>
        {/* Name / Logo */}
        <Box
          sx={{ textDecoration: "none", color: "inherit" }}
          component={Link}
          children={<Logo />}
          href="/"
        />

        {/* Spacer */}
        <Box sx={{ flexGrow: 1 }} component="span" />

        {/* Close button */}
        <IconButton component={Link} href="/">
          <FaCross />
        </IconButton>
      </div>
    </div>
  );
}
