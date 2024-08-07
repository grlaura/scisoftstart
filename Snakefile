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
        expand(f"results/{dirname}/{{image}}.json", image=DATA),
        expand(f"results/{dirname}/{{image}}_to_gt.json", image=DATA)

# process one of our images
rule process_image:
    input:
        script='src/Python/proccessImg.py',
        image=f'data/{dirname}/images/{{image}}.png'
    output: f'results/{dirname}/{{image}}.json'
    shell: 'python {input.script} {input.image} > {output}'

# compare results to ground truth
rule compare_to_ground_truth:
    input:
        script='src/Python/compareResultToGT.py',
        result_file=f'results/{dirname}/{{image}}.json',
        gt_file=f'data/{dirname}/ground_truth/{{image}}.json'
    output: f'results/{dirname}/{{image}}_to_gt.json'
    shell: 'python {input.script} {input.result_file} {input.gt_file} > {output}'
