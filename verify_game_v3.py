from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 800, 'height': 600})

        # Override CSS to ensure canvas is at 0,0
        page.add_style_tag(content="""
            body { margin: 0; padding: 0; display: block; height: 600px; width: 800px; }
            #game-container { margin: 0; padding: 0; position: absolute; top: 0; left: 0; border: none; box-shadow: none; }
        """)

        # 1. Start Screen
        print("Navigating to Start Screen...")
        page.goto("http://localhost:8080/index.html")
        time.sleep(1)
        page.screenshot(path="verification_1_start_map.png")
        print("Screenshot 1: Start Screen (Map)")

        # 2. Select USA (120, 140) - Click pin
        print("Selecting USA...")
        page.mouse.move(120, 140)
        time.sleep(0.5)
        page.screenshot(path="verification_2_hover_usa.png") # Verify Massive Hover Card
        page.mouse.click(120, 140)
        time.sleep(0.5)
        page.screenshot(path="verification_3_hub.png")
        print("Screenshot 3: Hub Screen")

        # 3. Go to Roster (50, 400)
        print("Going to Roster...")
        page.mouse.click(160, 425)
        time.sleep(0.5)
        page.screenshot(path="verification_4_roster.png")
        print("Screenshot 4: Roster Screen")

        # 4. Select Athlete
        print("Selecting Athlete...")
        page.mouse.click(400, 180) # First item in list
        time.sleep(0.5)
        page.screenshot(path="verification_5_detail.png")
        print("Screenshot 5: Athlete Detail")

        # 5. Train
        print("Training...")
        # Train button at 250, 380, w300 h80 -> center 400, 420
        page.mouse.click(400, 420)
        time.sleep(0.5)
        page.screenshot(path="verification_6_training_race.png")
        print("Screenshot 6: Training Race")

        # 6. Finish Training
        print("Finishing Training...")
        page.evaluate("race.distance = 99;")
        time.sleep(2.5) # Wait for finish and results transition
        page.screenshot(path="verification_7_results.png")
        print("Screenshot 7: Training Results")

        browser.close()

if __name__ == "__main__":
    run()
