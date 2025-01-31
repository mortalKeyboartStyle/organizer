# ui/bookmarks/nettools/container_env.py
import subprocess
import time

def run_ephemeral_container(image_name="ubuntu:latest", lifetime=30):
    """
    Uruchamia kontener z podanym obrazem, czeka X sekund, usuwa kontener.
    W realnym użyciu -> docker run -d ...
    """
    try:
        container_id = subprocess.check_output(
            ["docker", "run", "-d", image_name, "sleep", str(lifetime)],
            text=True
        ).strip()
        msg = f"[ContainerEnv] Uruchomiono kontener: {container_id} na {lifetime}s"
        # Można dodać pętlę monitorującą, etc.
        time.sleep(lifetime + 5)  # czekamy, by kontener się zakończył
        # lub docker rm -f
        return msg + "\nKontener powinien się zakończyć automatycznie."
    except Exception as e:
        return f"[ContainerEnv] Błąd: {e}"
