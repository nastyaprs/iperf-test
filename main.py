import subprocess


def client(server_ip):

    try:
        command = f"iperf -c {server_ip} -t 10"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout, stderr = process.communicate()

        return stdout.decode(), stderr.decode()
    except Exception as e:
        return '', str(e)
