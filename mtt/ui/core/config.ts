export type EnvName = "prod" | "test" | "local";
export type Config = {
  app: {
    env: EnvName;
    name: string;
    origin: string;
    hostname: string;
  };
};

export const config = {
  app: {
    env: "local",
    name: "React App",
    hostname: "localhost",
    origin: "http://localhost",
    api_origin: "http://localhost/api",
  },
};