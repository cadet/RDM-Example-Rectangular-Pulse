from cadetrdm import process_example, Options

if __name__ == "__main__":
    options = Options()
    options.commit_message = "Commit Message Test"
    options.debug = False
    options.push = False
    options.source_directory = "src"
    options.branch_prefix = "Experiment_A"
    process_example(options)
