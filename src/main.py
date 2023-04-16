import os

import generator
from args import get_args
from dataloader import load_data

# Load command line arguments
args = get_args()

# Remove file from last run if it exists
if os.path.exists(args.outputFilepath):
    os.remove(args.outputFilepath)

# Load cards as pairs
pairs = load_data(args.filename)

# Generate document
out = generator.generate(pairs)

# Save document
out.save(args.outputFilepath)
