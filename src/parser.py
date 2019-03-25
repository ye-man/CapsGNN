

import argparse

def parameter_parser():
    """
    A method to parse up command line parameters. By default it learns on the Erdos-Renyi dataset.
    The default hyperparameters give good results without cross-validation.
    """

    parser = argparse.ArgumentParser(description = "Run GAM.")
	
    parser.add_argument("--train-graph-folder",
                        nargs = "?",
                        default = "./input/train/",
	                help = "Training graphs folder.")

    parser.add_argument("--test-graph-folder",
                        nargs = "?",
                        default = "./input/test/",
	                help = "Testing graphs folder.")

    parser.add_argument("--prediction-path",
                        nargs = "?",
                        default = "./output/watts_predictions.csv",
	                help = "Path to store the predicted graph labels.")

    parser.add_argument("--epochs",
                        type = int,
                        default = 10,
	                help = "Number of training epochs. Default is 10.")

    parser.add_argument("--batch-size",
                        type = int,
                        default = 32,
	                help = "Number of graphs processed per batch. Default is 32.")

    parser.add_argument("--gcn-filters",
                        type = int,
                        default = 2,
	                help = "Discount for correct predictions. Default is 0.99.")

    parser.add_argument("--gcn-layers",
                        type = int,
                        default = 5,
	                help = "Number of Graph Convolutional Layers. Default is 0.001.")

    parser.add_argument("--inner-attention-dimension",
                        type = int,
                        default = 20,
	                help = "Number of Graph Convolutional Layers. Default is 0.001.")

    parser.add_argument("--capsule-dimensions",
                        type = int,
                        default = 7,
	                help = "Number of Graph Convolutional Layers. Default is 0.001.")

    parser.add_argument("--number-of-capsules",
                        type = int,
                        default = 5,
	                help = "Number of Graph Convolutional Layers. Default is 0.001.")

    parser.add_argument("--weight-decay",
                        type = float,
                        default = 10**-6,
	                help = "Learning rate. Default is 10^-5.")

    parser.add_argument("--learning-rate",
                        type = float,
                        default = 0.01,
	                help = "Learning rate. Default is 10^-5.")

    parser.add_argument("--lambd",
                        type = float,
                        default = 1.0,
	                help = "Learning rate. Default is 10^-5.")
    
    
    return parser.parse_args()
