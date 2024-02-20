import { Box, Container, Typography } from "@mui/joy";
import { usePageEffect } from "../core/page.js";

export function Component(): JSX.Element {
  usePageEffect({ title: "React Apps" });

  return (
    <Container
      sx={{
        py: "20vh",
        border: "1px solid #e0e0e0",
        borderRadius: "8px",
        background: "linear-gradient(45deg, #FAFAFA, #E0E0E0)",
      }}
      maxWidth="sm"
    >
      <Typography
        sx={{ mb: 2, fontWeight: "bold", lineHeight: 1.2 }}
        variant="h1"
        align="center"
      >
        Welcome to MTT
      </Typography>

      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          gridGap: "1rem",
          mt: 4,
        }}
      >
        index page
      </Box>
    </Container>
  );
}

Component.displayName = "IndexPage";
