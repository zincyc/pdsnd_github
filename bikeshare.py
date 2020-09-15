import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

WEEKDAY_NAME = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ''
    while city not in CITY_DATA:
        city = input('Would you like to see the data for Chicago, New York City or Washington? ').lower()
        if city in CITY_DATA:
            continue
        else:
            print('You have input an invalid input. Please try again.')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    month = ''
    while month not in MONTHS:
        month = input().lower()
        if month in MONTHS:
            print('Would you like to see the data by which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?')
        else:
            print('You have input an invalid input. Please try again.')

    # TO DO: get user input for month (all, january, february, ... , june)
    day = ''
    while day not in WEEKDAY_NAME:
        day = input().lower()
        if day in WEEKDAY_NAME:
            print('Analysing data...')
        else:
            print('You have input an invalid input. Please try again.')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    common_month = MONTHS[common_month -1].title()
    print('The most common month is {}.'.format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is {}.'.format(common_day))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is {}.'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}.'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most commonly used end station is {}.'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['com'] = df['Start Station'] + ' and ' + df['End Station']
    common_com = df['com'].mode()[0]
    print('The most frequent combination of start station and end station is {}.'.format(common_com))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum(axis=0)
    print('Total travel time: {}.'.format(total_trip_duration))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean(axis=0)
    print('Mean travel time: {}.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('Count of user types: {}.'.format(user_types))

    except:
        print('There is no data for user types.')

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Counts of gender: {}.'.format(gender))

    except:
        print('There is no data for gender.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        i, j, k = df['Birth Year'].min(axis=0), df['Birth Year'].max(axis=0), df['Birth Year'].mode()[0]
        print('The earliest birth year: {}.'.format(i))
        print('The most recent birth year: {}.'.format(j))
        print('The most common birth year: {}.'.format(k))

    except:
        print('There is no data for birth year.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:5 + start_loc])
        start_loc += 5
        view_display = input('Do you wish to continue?: ').lower()
        if view_display == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
