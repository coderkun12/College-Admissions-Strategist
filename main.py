# Entry points to run FastAPI server. 
import subprocess
import multiprocessing
import time

def run_api():
    # Runs the FastAPI server
    subprocess.run(["python", "-m", "app.api"])

def run_ui():
    # Runs the Chainlit interface
    # Note: Chainlit usually needs the 'chainlit run' command
    subprocess.run(["chainlit", "run", "app/ui.py", "--port", "8000"])

if __name__ == "__main__":
    print("🚀 Starting Admissions Strategist System...")
    
    # Create processes for both
    api_process = multiprocessing.Process(target=run_api)
    ui_process = multiprocessing.Process(target=run_ui)

    # Start the api and UI files for execution.
    api_process.start()
    time.sleep(2) 
    ui_process.start()

    # Join the api and ui processes so that they can coordinate. 
    api_process.join()
    ui_process.join()