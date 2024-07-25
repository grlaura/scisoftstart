# Snakefile
# Load configuration
configfile: "config.yaml"
dirname = config["dataset"]

# a list of all the books we are analyzing
# {{}} placeholders for variable substitution within strings
DATA = glob_wildcards(f'data/{dirname}/images/{{image}}.png').image

print(f"dirname: {dirname}")
print(f"DATA: {DATA}")

rule all:
    input:
        expand(f"results/{dirname}/{{image}}.json", image=DATA)

# process one of our images
rule process_image:
    input:
        script='src/Python/proccessImg.py',
        image=f'data/{dirname}/images/{{file}}.png'
    output: f'results/{dirname}/{{file}}.json'
    shell: 'python {input.script} {input.image} > {output}'
