import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# functions below

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ' '
    while city not in CITY_DATA:
        city = input('choose a city by inputing \'chicago\', \'new york city\' or \'washington\': \n').lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ' '
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "all"]
    while month not in months:
        month = input('input a month you want to filter by. \'all\' is a valid option\n').lower()
      
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ' '
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    while day not in days:
        day = input('input a days you want to filter by. \'all\' is a valid option\n').lower()
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
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    df['hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m = df.month.mode()[0]
    print(f'most common month: {m}')

    # TO DO: display the most common day of week
    dow = df.day_of_week.mode()[0]
    print(f'most common day of week: {dow}')

    # TO DO: display the most common start hour
    h = df.hour.mode()[0]
    print(f'most common start hour: {h}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    ss = df['Start Station'].mode()[0]
    print(f'most commonly used start station: {ss}')

    # TO DO: display most commonly used end station
    es = df['End Station'].mode()[0]
    print(f'most commonly used end station: {es}')

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    trip = df.trip.mode()[0]
    print(f'most frequent combination of start station and end station trip: {trip}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"total travel time (in seconds) is {df['Trip Duration'].sum():.2f}")
    # TO DO: display mean travel time
    print(f"mean travel time (in seconds) is {df['Trip Duration'].mean():.2f}")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"counts of user types is:\n{df['User Type'].value_counts()}")
    

    # TO DO: Display counts of gender
    if city != 'washington':
        print(f"counts of gender is:\n{df['Gender'].value_counts()}")
    else: 
        print('Washington does not have Gender data')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print(f"earliest year of birth is: {df['Birth Year'].min():.0f}")
        print(f"most recent year of birth is: {df['Birth Year'].max():.0f}")
        print(f"most common year of birth year of birth is: {df['Birth Year'].mode()[0]:.0f}")
        
    else:
        print('Washington does not have birth year data for users')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        see_data = ' '
        while see_data not in ['yes','no']:
            see_data = input('Would you like to see first 5 line of data (yes/no)?\n').lower()
            loc = 0
            if see_data == 'yes':
                print(df.iloc[loc : loc+5])
                loc += 5
                see_more = ' '
                while True:
                    see_more = input('Would you like to see next 5 line of data (yes/no)?\n')
                    if see_more == 'yes':
                        print(df.iloc[loc : loc+5])
                        loc += 5
                    elif see_more == 'no':
                        break
                    else: print()
            elif see_data == 'no':
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
