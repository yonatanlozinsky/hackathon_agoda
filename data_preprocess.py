import numpy as np


def clean_data(data_frame):
    """
    Clean data
    :param data_frame:
    :return:
    """
    # standardize all NaN values
    NaN_values = ['NA', 'N/A', "inf", "nan", "na", None, "NaN"]
    data_frame.replace(NaN_values, np.nan)

    # handle rating values
    rating_mask = (data_frame.hotel_star_rating >= 0) & (data_frame.hotel_star_rating <= 5)
    data_frame = data_frame[rating_mask]  # remove bad ratings (negative, nan and more), maybe it's better to put mean

    data_frame = data_frame[data_frame.hotel_country_code.notna()]  # NaN country code should be removed

    # TODO: make request_highfloor, request_largebed, request_twinbeds, request_airport, request_earlycheckin
    #  a dummy variable?

    return None
