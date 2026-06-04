"""Functions to help Guido plan and prepare a nice lasagna."""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(min_in_oven):
    """Calculate the bake time remaining.

    Parameters:
        min_in_oven (int): The time already spent baking in minutes.
    Returns:
        int: The remaining bake time in minutes.
    """
    time_remaining = EXPECTED_BAKE_TIME - min_in_oven
    return time_remaining

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
    Returns:
        int: Total time spent in preparation in minutes.
    """
    preparation_time = number_of_layers * 2
    return preparation_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time already spent baking in the oven.
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.
    """
    total_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_time

if __name__ == "__main__":
    layers = 3
    baked_so_far = 15

    print(f"Expected bake time: {EXPECTED_BAKE_TIME} minutes")
    print(f"Bake time remaining: {bake_time_remaining(baked_so_far)} minutes")
    print(f"Preparation time for {layers} layers: {preparation_time_in_minutes(layers)} minutes")
    print(f"Total elapsed time: {elapsed_time_in_minutes(layers, baked_so_far)} minutes")