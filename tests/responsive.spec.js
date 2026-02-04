import { test, expect } from '@playwright/test';

// Define viewports to test
const viewports = {
  mobile: { width: 375, height: 667, name: 'mobile' },
  tablet: { width: 768, height: 1024, name: 'tablet' },
  desktop: { width: 1440, height: 900, name: 'desktop' },
};

// Test each breakpoint
Object.entries(viewports).forEach(([key, viewport]) => {
  test(`Homepage - ${viewport.name} (${viewport.width}x${viewport.height})`, async ({ browser }) => {
    const context = await browser.newContext({
      viewport: { width: viewport.width, height: viewport.height },
      deviceScaleFactor: 1,
    });
    const page = await context.newPage();

    // Navigate to homepage
    await page.goto('http://localhost:4000/petersalvato-constellation/', { waitUntil: 'networkidle' });

    // Take screenshot
    await page.screenshot({ path: `tests/screenshots/${viewport.name}-homepage.png`, fullPage: true });

    // Check hamburger visibility on mobile
    if (viewport.name === 'mobile') {
      const hamburger = page.locator('.hamburger-icon');
      await expect(hamburger).toBeVisible();
      console.log('✓ Hamburger visible on mobile');

      // Test hamburger interaction
      await hamburger.click();
      const sidebar = page.locator('#sidebar-nav');
      await expect(sidebar).toBeVisible();
      console.log('✓ Hamburger toggles sidebar');

      // Click a nav link to close menu
      const navLink = page.locator('.nav-list a').first();
      await navLink.click();
      await page.waitForTimeout(500); // Wait for animation
      // Check if details element is closed
      const detailsOpen = await page.locator('#sidebar-toggle').evaluate(el => el.open);
      console.log(`Details open state: ${detailsOpen}`);
    }

    // Check hamburger hidden on tablet/desktop
    if (viewport.name === 'tablet' || viewport.name === 'desktop') {
      const hamburger = page.locator('.hamburger-icon');
      await expect(hamburger).not.toBeVisible();
      console.log(`✓ Hamburger hidden on ${viewport.name}`);

      // Check sidebar visible
      const sidebar = page.locator('#sidebar-nav');
      await expect(sidebar).toBeVisible();
      console.log(`✓ Sidebar visible on ${viewport.name}`);
    }

    // Check main content exists and is readable
    const mainContent = page.locator('#main-content');
    await expect(mainContent).toBeVisible();
    console.log(`✓ Main content visible on ${viewport.name}`);

    // Check typography is readable (not too small)
    const h1 = page.locator('h1').first();
    const fontSize = await h1.evaluate(el => window.getComputedStyle(el).fontSize);
    console.log(`  H1 font-size on ${viewport.name}: ${fontSize}`);

    // Check if layout is responsive (no horizontal scroll)
    const bodyWidth = await page.evaluate(() => document.documentElement.scrollWidth);
    const viewportWidth = viewport.width;
    if (bodyWidth > viewportWidth) {
      console.log(`⚠ WARNING: Horizontal overflow on ${viewport.name}! Body: ${bodyWidth}px, Viewport: ${viewportWidth}px`);
    } else {
      console.log(`✓ No horizontal overflow on ${viewport.name}`);
    }

    await context.close();
  });

  // Test key pages at each breakpoint
  const testPages = [
    { path: '/protocols/portable-agency/', name: 'Protocol' },
    { path: '/systems/aiden-jae/', name: 'System' },
    { path: '/practice/colophon/', name: 'Practice' },
  ];

  testPages.forEach(({ path, name }) => {
    test(`${name} page - ${viewport.name}`, async ({ browser }) => {
      const context = await browser.newContext({
        viewport: { width: viewport.width, height: viewport.height },
      });
      const page = await context.newPage();

      await page.goto(`http://localhost:4000/petersalvato-constellation${path}`, { waitUntil: 'networkidle' });
      await page.screenshot({ path: `tests/screenshots/${viewport.name}-${name.toLowerCase()}.png`, fullPage: true });

      // Check for layout issues
      const bodyWidth = await page.evaluate(() => document.documentElement.scrollWidth);
      if (bodyWidth > viewport.width) {
        console.log(`⚠ ${name} - Horizontal overflow on ${viewport.name}`);
      } else {
        console.log(`✓ ${name} - No overflow on ${viewport.name}`);
      }

      // Check specs grids are responsive
      const specsGrid = page.locator('.protocol-specs, .system-specs').first();
      if (await specsGrid.isVisible()) {
        const gridCols = await specsGrid.evaluate(el => window.getComputedStyle(el).gridTemplateColumns);
        console.log(`  Grid columns on ${viewport.name}: ${gridCols}`);
      }

      await context.close();
    });
  });
});
