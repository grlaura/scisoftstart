# Snakefile
# Load configuration
configfile: "config.yaml"
dirname = config["dataset"]


# a list of all the books we are analyzing
DATA = glob_wildcards('data/{dirname}/{image}.png').image


rule all:
    input:
        expand("results/{dirname}/{image}.json", dirname = dirname, image=DATA)

# process one of our images
rule process_image:
    input:
        script='src/Python/proccessImg.py',
        image='data/{dirname}/{file}.png'
    output: 'results/{dirname}/{file}.json'
    shell: 'python {input.script} {input.image} > {output}'
