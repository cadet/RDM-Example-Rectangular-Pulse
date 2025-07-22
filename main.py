from cadetrdm import process_example, Options

if __name__ == "__main__":
    options = Options()
    options.commit_message = "Commit Message Test"
    options.debug = True
    options.push = True
    options.source_directory = "src"
    options.branch_prefix = "Experiment_A"
    process_example(options)
