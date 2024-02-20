import { Link } from "@mui/joy";
import { Link as NavLink } from "../../common/Link.js";
import { Logo } from "./Logo.js";

export function AppToolbar(props: any): JSX.Element {
  const { sx, ...other } = props;

  return (
    <div color="default" elevation={1} {...other}>
      {/* App name / logo */}

      <Link
        style={{ paddingLeft: 20, paddingTop: 20 }}
        color="inherit"
        underline="none"
        href="/"
        component={NavLink}
      >
        <Logo />
      </Link>

      <span style={{ flexGrow: 1 }} />

      {/* Account related controls (icon buttons) */}

      {/* Pop-up menus */}
    </div>
  );
}
