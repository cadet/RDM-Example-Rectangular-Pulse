from cadetrdm import process_example, Options

if __name__ == "__main__":
    options = Options()
    options.commit_message = "Process example"
    options.debug = False
    options.push = True
    options.source_directory = "src"
    process_example(options)
