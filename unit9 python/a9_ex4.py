import argparse
import subprocess

def run_program(program, args, timeout):
    try:
        if args:
            args_str = ' '.join(args)
            print(f"Running program '{program}' with arguments {args_str} with a {timeout}s timeout")
            result = subprocess.run([program] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
        else:
            print(f"Running program '{program}' without any arguments with a {timeout}s timeout")
            result = subprocess.run([program], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
        
        print(f"The '{program}' finished with exit code {result.returncode}")

        if result.stderr:
            print(f"The '{program}' produced the following error output:")
            print(result.stderr)

        if result.stdout:
            print(f"The '{program}' produced the following standard output:")
            print(result.stdout)

    except FileNotFoundError:
        print(f"The specified program '{program}' could not be found")
    except subprocess.TimeoutExpired:
        print("The program execution timed out")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Execute arbitrary programs with arguments.')
    parser.add_argument('-p', '--program', type=str, required=True, help='Name of the program to be executed.')
    parser.add_argument('-a', '--args', nargs='+', default=[], help='Arguments to be passed to the program.')
    parser.add_argument('-t', '--timeout', type=float, default=60, help='Timeout in seconds for the execution of the program.')
    args = parser.parse_args()

    run_program(args.program, args.args, args.timeout)
