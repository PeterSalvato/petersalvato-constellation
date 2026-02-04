import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: false,
  retries: 0,
  workers: 1,
  reporter: [
    ['html', { outputFolder: 'test-results' }],
    ['list'],
  ],
  use: {
    baseURL: 'http://localhost:4000',
    trace: 'on-first-retry',
    screenshot: 'off',
  },
  webServer: null, // We'll start Jekyll manually
  timeout: 30000,
});
