import argparse
import subprocess

def execute_program(program, args, timeout):
    try:
        full_command = [program] + args
        if args:
            print(f"Running program '{program}' with arguments {full_command} with a {timeout}s timeout")
        else:
            print(f"Running program '{program}' without any arguments with a {timeout}s timeout")
        
        result = subprocess.run(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)

        if result.returncode == 0:
            print(f"The '{program}' finished with exit code {result.returncode}")
            if result.stdout:
                print(f"The '{program}' produced the following standard output:\n{result.stdout}")
        else:
            print(f"The '{program}' finished with exit code {result.returncode}")
            if result.stderr:
                print(f"The '{program}' produced the following error output:\n{result.stderr}")

    except FileNotFoundError:
        print(f"The specified program '{program}' could not be found")

    except subprocess.TimeoutExpired:
        print("The program execution timed out")

def main():
    parser = argparse.ArgumentParser(description="Execute arbitrary programs with arguments.")
    parser.add_argument('-p', '--program', type=str, required=True, help="Name of the program to be executed.")
    parser.add_argument('-a', '--args', nargs='+', default=[], help="Arguments to be passed to the program.")
    parser.add_argument('-t', '--timeout', type=float, default=60, help="Timeout in seconds for the execution of the program.")
    
    args = parser.parse_args()
    execute_program(args.program, args.args, args.timeout)

if __name__ == "__main__":
    main()