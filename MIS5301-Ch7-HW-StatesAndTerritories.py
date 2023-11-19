#------------------------------------------------------------
#Name: Monroy, Noah
#MIS 5301 – Fall 2023
#Purpose: U.S. States and Territories Data
#File: MIS5301-Ch7-HW-StatesAndTerritories.py
#------------------------------------------------------------

#Global Constants


#1D Lists ------------------------------------------------------------------------------------------------------------------
STATE_CODES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
               'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
               'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

TERRITORY_CODES = ['AS', 'GU', 'MP', 'PR', 'VI']


STATE_INCOMES = [56929, 81133, 70821, 50784, 81575, 84954, 80958, 68687, 59734, 61497,
                  82199, 76918, 79253, 70190, 72429, 75979, 55629, 57206, 71139, 97332,
                  86566, 64488, 80441, 46637, 63594, 64999, 78109, 64340, 88841, 88559,
                  53463, 72920, 62891, 68882, 62689, 60096, 81855, 72627, 74982, 62542,
                  73893, 62166, 67404, 87649, 76079, 80268, 87648, 46836, 69943, 71052]
    
#2D LISTs ------------------------------------------------------------------------------------------------------------------
STATES = [  ['AL' , 'Alabama' , 'Montgomery' , 'Yellowhammer' , 'Camellia' , 22 , '12/14/1819' , 5024279],
            ['AK' , 'Alaska' , 'Juneau' , 'Willow Ptarmigan' , 'Forget-me-not' , 49 , '01/03/1959' , 733391],
            ['AZ' , 'Arizona' , 'Phoenix' , 'Cactus Wren' , 'Saguaro Cactus Blossom' , 48 , '02/14/1912' , 7151502],
            ['AR' , 'Arkansas' , 'Little Rock' , 'Mockingbird' , 'Apple Blossom' , 25 , '06/15/1836' , 3011524],
            ['CA' , 'California' , 'Sacramento' , 'California Valley Quail' , 'Golden Poppy' , 31 , '09/09/1850' , 39538223],
            ['CO' , 'Colorado' , 'Denver' , 'Lark Bunting' , 'Columbine' , 38 , '08/01/1876' , 5773714],
            ['CT' , 'Connecticut' , 'Hartford' , 'American Robin' , 'Mountain Laurel' , 5 , '01/09/1788' , 3605944],
            ['DE' , 'Delaware' , 'Dover' , 'Blue Hen Chicken' , 'Peach Blossom' , 1 , '12/07/1787' , 989948],
            ['FL' , 'Florida' , 'Tallahassee' , 'Mockingbird' , 'Orange Blossom' , 27 , '03/03/1845' , 21538187],
            ['GA' , 'Georgia' , 'Atlanta' , 'Brown Thrasher' , 'Cherokee Rose' , 4 , '01/02/1788' , 10711908],
            ['HI' , 'Hawaii' , 'Honolulu' , 'Nene (Hawaiian Goose)' , 'Hibiscus' , 50 , '08/21/1959' , 1455271],
            ['ID' , 'Idaho' , 'Boise' , 'Mountain Bluebird' , 'Syringa' , 43 , '07/03/1890' , 1839106],
            ['IL' , 'Illinois' , 'Springfield' , 'Cardinal' , 'Native violet' , 21 , '12/03/1818' , 12812508],
            ['IN' , 'Indiana' , 'Indianapolis' , 'Cardinal' , 'Peony' , 19 , '12/11/1816' , 6785528],
            ['IA' , 'Iowa' , 'Des Moines' , 'Eastern Goldfinch' , 'Wild Rose' , 29 , '12/28/1846' , 3190369],
            ['KS' , 'Kansas' , 'Topeka' , 'Western Meadowlark' , 'Native Sunflower' , 34 , '01/29/1861' , 2937880],
            ['KY' , 'Kentucky' , 'Frankfort' , 'Kentucky Cardinal' , 'Goldenrod' , 15 , '06/01/1792' , 4505836],
            ['LA' , 'Louisiana' , 'Baton Rouge' , 'Pelican' , 'Magnolia' , 18 , '04/30/1812' , 4657757],
            ['ME' , 'Maine' , 'Augusta' , 'Chickadee' , 'White Pine Cone and Tassel' , 23 , '03/15/1820' , 1362359],
            ['MD' , 'Maryland' , 'Annapolis' , 'Baltimore Oriole' , 'Black-Eyed Susan' , 7 , '04/28/1788' , 6177224],
            ['MA' , 'Massachusetts' , 'Boston' , 'Chickadee' , 'Mayflower' , 6 , '02/06/1788' , 7029917],
            ['MI' , 'Michigan' , 'Lansing' , 'Robin' , 'Apple Blossom' , 26 , '01/26/1837' , 10077331],
            ['MN' , 'Minnesota' , 'St. Paul' , 'Common Loon' , 'Pink and White Ladys Slipper' , 32 , '05/11/1858' , 5706494],
            ['MS' , 'Mississippi' , 'Jackson' , 'Mockingbird' , 'Magnolia' , 20 , '12/10/1817' , 2961279],
            ['MO' , 'Missouri' , 'Jefferson City' , 'Bluebird' , 'Hawthorn' , 24 , '08/10/1821' , 6154913],
            ['MT' , 'Montana' , 'Helena' , 'Western Meadowlark' , 'Bitterroot' , 41 , '11/08/1889' , 1084225],
            ['NE' , 'Nebraska' , 'Lincoln' , 'Western Meadowlark' , 'Goldenrod' , 37 , '03/01/1867' , 1961504],
            ['NV' , 'Nevada' , 'Carson City' , 'Mountain Bluebird' , 'Sagebrush' , 36 , '10/31/1864' , 3104614],
            ['NH' , 'New Hampshire' , 'Concord' , 'Purple Finch' , 'Purple Lilac' , 9 , '06/21/1788' , 1377529],
            ['NJ' , 'New Jersey' , 'Trenton' , 'Eastern Goldfinch' , 'Purple Violet' , 3 , '12/18/1787' , 9288994],
            ['NM' , 'New Mexico' , 'Santa Fe' , 'Roadrunner' , 'Yucca Flower' , 47 , '01/06/1912' , 2117522],
            ['NY' , 'New York' , 'Albany' , 'Bluebird' , 'Rose' , 11 , '07/26/1788' , 20201249],
            ['NC' , 'North Carolina' , 'Raleigh' , 'Cardinal' , 'Dogwood' , 12 , '11/21/1789' , 10439388],
            ['ND' , 'North Dakota' , 'Bismarck' , 'Western Meadowlark' , 'Wild Prairie Rose' , 39 , '11/02/1889' , 779094],
            ['OH' , 'Ohio' , 'Columbus' , 'Cardinal' , 'Scarlet Carnation' , 17 , '03/01/1803' , 11799448],
            ['OK' , 'Oklahoma' , 'Oklahoma City' , 'Scissor-Tailed Flycatcher' , 'Mistletoe' , 46 , '11/16/1907' , 3959353],
            ['OR' , 'Oregon' , 'Salem' , 'Western Meadowlark' , 'Oregon Grape' , 33 , '02/14/1859' , 4237256],
            ['PA' , 'Pennsylvania' , 'Harrisburg' , 'Ruffed Grouse' , 'Mountain Laurel' , 2 , '12/12/1787' , 13002700],
            ['RI' , 'Rhode Island' , 'Providence' , 'Rhode Island Red' , 'Violet' , 13 , '05/29/1790' , 1097379],
            ['SC' , 'South Carolina' , 'Columbia' , 'Carolina Wren' , 'Yellow Jessamine' , 8 , '05/23/1788' , 5118425],
            ['SD' , 'South Dakota' , 'Pierre' , 'Ring-Necked Pheasant' , 'American Pasqueflower' , 40 , '11/02/1889' , 886667],
            ['TN' , 'Tennessee' , 'Nashville' , 'Mockingbird' , 'Iris' , 16 , '06/01/1796' , 6910840],
            ['TX' , 'Texas' , 'Austin' , 'Mockingbird' , 'Bluebonnet' , 28 , '12/29/1845' , 29145505],
            ['UT' , 'Utah' , 'Salt Lake City' , 'California Gull' , 'Sego Lily' , 45 , '01/04/1896' , 3271616],
            ['VT' , 'Vermont' , 'Montpelier' , 'Hermit Thrush' , 'Red Clover' , 14 , '03/04/1791' , 643077],
            ['VA' , 'Virginia' , 'Richmond' , 'Cardinal' , 'Dogwood' , 10 , '06/25/1788' , 8631393],
            ['WA' , 'Washington' , 'Olympia' , 'Willow Goldfinch' , 'Western Rhododendron' , 42 , '11/11/1889' , 7705281],
            ['WV' , 'West Virginia' , 'Charleston' , 'Cardinal' , 'Big Rhododendron' , 35 , '06/20/1863' , 1793716],
            ['WI' , 'Wisconsin' , 'Madison' , 'Robin' , 'Wood Violet' , 30 , '05/29/1848' , 5893718],
            ['WY' , 'Wyoming' , 'Cheyenne' , 'Meadowlark' , 'Indian Paintbrush' , 44 , '07/10/1890' , 576851]]


TERRITORIES = [ ['AS' , 'American Samoa' , 'Pago Pago' , '1900' , 49710],
                ['GU' , 'Guam' , 'Hagåtña' , '1899' , 153836],
                ['MP' , 'Northern Mariana Islands' , 'Saipan' , '1986' , 47329],
                ['PR' , 'Puerto Rico' , 'San Juan' , '1899' , 3285874],
                ['VI' , 'U.S. Virgin Islands' , 'Charlotte Amalie' , '1917' , 87146]]


#MAIN ------------------------------------------------------------------------------------------------------------------

def main():

    #initialize local constants
    APP_NAME = 'U.S. States & Territories'

    #initialize variables
    stars = '*' * 70
    indent1 = '   '
    dashes = '-' *25

    #indefinite while loop
    selection = ''
    
    while selection != 'X':
        print()
        print(indent1 + 'Menu Options')
        print(indent1 + dashes)
        print(indent1 + "1: View all states")
        print(indent1 + "2: View all territories")
        print(indent1 + "3: View one state")
        print(indent1 + "4: View state stats & facts")
        print(indent1 + "X: Press to exit")
        print()
        selection = str(input(f'{indent1}Enter a selection: ').upper())

        #validate input
        while selection not in ['1','2','3','4','X']:
            print('\t>> Enter a valid selection.')
            selection = str(input(f'{indent1}Enter a selection: ').upper())
    

        #call fn1
        if selection == '1':
            view_all_states()

        #call fn2
        if selection == '2':
            view_territories()
        
        #call fn3
        if selection == '3':
            state_code = str(input(f'{indent1}Enter a state code: ').upper())
        
            #validate fn3
            while state_code not in STATE_CODES:
                print('\t>> Enter a valid state code.')
                state_code = str(input(f'{indent1}Enter a state code: ').upper())

            view_one_state(state_code)

        #call fn4
        if selection == '4':
            view_stats_facts()

        #Call exit
        if selection == 'X':
            print()
            print("Thank you for using Victorino's U.S. States & Territories application.")
     
        print()
    

#FUNCTIONS -------------------------------------------------------------------------------------------------------------

#FN: Header
def header(APP_NAME):
    stars = '*' * 70
    print(stars)
    print(f'{APP_NAME:^70}')
    print(stars)
    
###FN 1: 1) view all states
def view_all_states():
    equals = '=' *25
    print()
    print(equals)
    print(' List of States')
    print(equals)
    print()
    print(f'{"Code":4} {"State Name":14} {"Capital":14} {"Join Order":10} {"Join Date":10} {"Bird":25} {"Flower":28} {"Population":10}')
    print(('-'*4), ('-'*14), ('-'*14), ('-'*10), ('-'*10), ('-'*25), ('-'*28), ('-'*10))

    #loop through
    for row in STATES:
        state_code = row[0]
        state_name = row[1]
        state_cap = row [2]
        join_order = row[5]
        join_date = row[6]
        bird = row[3]
        flower = row[4]
        population = row[7]
        
        print(f'{state_code:^4} {state_name:14} {state_cap:14} {join_order:^10} {join_date:^10} {bird:25} {flower:28} {population:10,}')

    print()
    input('Press enter to continue...')
    
#FN 2: 2) View territories  
def view_territories():
    equals = '=' *25
    print()
    print(equals)
    print(' List of Territories')
    print(equals)
    print()
    print(f'{"Code":4} {"Territory Name":25} {"Capital":16} {"Year":4} {"Population":10}')
    print(('-'*4), ('-'*25), ('-'*16), ('-'*4), ('-'*10))

    #loop through
    for row in TERRITORIES:
        t_code = row[0]
        t_name = row[1]
        t_cap = row[2]
        t_year = row[3]
        t_pop = row[4]

        print(f'{t_code:^4} {t_name:25} {t_cap:16} {t_year:4} {t_pop:10}')
    print()
    input('Press enter to continue...')
            

#FN 3: 3) View one state
def view_one_state(state_code):
    equals = '=' *25
    print()
    print(equals)
    print(' State Details')
    print(equals)
    print()
    longequals = '-' * 35
    print(longequals)

    #loop
    for i in range(0, len(STATES)):
        if STATES[i][0] == state_code:
            print(f'{"State:":12} {STATES[i][0]} - {STATES[i][1]}')
            print(f'{"Capital:":12} {STATES[i][2]}')
            print(f'{"Bird:":12} {STATES[i][3]}')
            print(f'{"Flower:":12} {STATES[i][4]}')
            print(f'{"Join Order:":12} {STATES[i][5]}')
            print(f'{"Join Date:":12} {STATES[i][6]}')
            print(f'{"Population:":12} {STATES[i][7]:,}')
            print(f'{"Avg Income:":12} ${STATE_INCOMES[i]:,}')
    print()
    input('Press enter to continue...')

#FN 4: 4) display stats & facts
def view_stats_facts():
    equals = '=' *25
    longequals = '-' * 35
    tab = '     '
    total_population = 0
    min_population = 10000000000
    max_population = 0
    first_state = ''
    last_state = ''
    mockingbird_states = 0
    first_state_date = ''
    
    print()
    print(equals)
    print(' All States - Stats & Facts')
    print(equals)
    print()
    print(longequals)
    print('  Population Stats:')

    #loop
    for row in STATES:
        state_code = row[0]
        state_name = row[1]
        state_cap = row [2]
        bird = row[3]
        flower = row[4]
        join_order = row[5]
        join_date = row[6]
        population = row[7]
    
        total_population += row[7]
        avg_per_state = round(total_population / 50)
        

        # min population
        if population < min_population:
            min_population = population
                
        # max population       
        if population > max_population:
            max_population = population

        #first state
        for i in range(0, len(STATES)):
            if join_order == 1:
                first_state = state_name
                first_state_date = join_date

        #last state
        for i in range(0, len(STATES)):
            if join_order == 50:
                last_state = state_name
                last_state_date = join_date
        
        #mockingbird states
        if bird == 'Mockingbird':
            mockingbird_states += 1
        
    print(f'{tab}{"Total:":15} {total_population:,}')
    print(f'{tab}{"Avg/State:":15} {avg_per_state:,}')
    print(f'{tab}{"Min:":15} {min_population:,}')
    print(f'{tab}{"Max:":15} {max_population:,}')
    
    print(longequals)
    print(f'{tab}Mockingbird States: {mockingbird_states}')
    print(longequals)
    
    print('  Join Order:')
    print(f'{tab}{"First:":15} {first_state} - {first_state_date}')
    print(f'{tab}{"Last:":15} {last_state} - {last_state_date}')
    
    print()
    input('Press enter to continue...')
    
main()





