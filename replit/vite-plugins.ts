/**
 * Replit-specific Vite plugins. Only active when running on Replit (REPL_ID set).
 * Import this from root vite.config.ts to keep Replit code out of the root.
 */
import runtimeErrorOverlay from "@replit/vite-plugin-runtime-error-modal";

export function getReplitPlugins(): Promise<import("vite").Plugin[]> {
  const isReplit =
    process.env.NODE_ENV !== "production" &&
    process.env.REPL_ID !== undefined;

  if (!isReplit) {
    return Promise.resolve([runtimeErrorOverlay()]);
  }

  return Promise.all([
    import("@replit/vite-plugin-cartographer").then((m) => m.cartographer()),
    import("@replit/vite-plugin-dev-banner").then((m) => m.devBanner()),
  ]).then((extra) => [runtimeErrorOverlay(), ...extra]);
}
