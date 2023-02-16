import random

# lista dostępnych hoteli
hotels = [
    {'name': 'Cancun Bay Resort', 'country': 'Meksyk', 'stars': '4/5', 'price': 450},
    {'name': 'Iberostar Quetzal', 'country': 'Meksyk', 'stars': '5/5', 'price': 690},
    {'name': 'Imperial Laguna by Faranda', 'country': 'Meksyk', 'stars': '3/5', 'price': 320},
    {'name': 'Playacalida', 'country': 'Hiszpania', 'stars': '5/5', 'price': 600},
    {'name': 'Palia Puerto del Sol', 'country': 'Hiszpania', 'stars': '3/5', 'price': 240},
    {'name': 'Playa Real Resort', 'country': 'Hiszpania', 'stars': '4/5', 'price': 380},
    {'name': 'Sea Gull', 'country': 'Egipt', 'stars': '3/5', 'price': 270},
    {'name': 'Continental Hurghada', 'country': 'Egipt', 'stars': '4/5', 'price': 360},
    {'name': 'Sharm Grand Plaza', 'country': 'Egipt', 'stars': '5/5', 'price': 620},
    {'name': 'Ikaros Hotel', 'country': 'Grecja', 'stars': '3/5', 'price': 220},
    {'name': 'Labranda Sandy Beach Resort', 'country': 'Grecja', 'stars': '5/5', 'price': 580},
    {'name': 'Lida Corfu', 'country': 'Grecja', 'stars': '4/5', 'price': 310},
    {'name': 'Mytt Beach Hotel', 'country': 'Tajlandia', 'stars': '5/5', 'price': 720},
    {'name': 'Novotel Rayong', 'country': 'Tajlandia', 'stars': '4/5', 'price': 410},
    {'name': 'Cholchan Pattaya Resort', 'country': 'Tajlandia', 'stars': '3/5', 'price': 290},
]


class Trip:
    def offers(hotels):
        offers_a = [random.choice(hotels),random.choice(hotels),random.choice(hotels)]
        sorted_hotels = sorted(offers_a, key=lambda x: x['price'])
        days = random.choice([7, 10, 14])
        date = ''
        match days:
            case 7:
                date = '22.06.2022'
            case 10:
                date = '25.06.2022'
            case 14:
                date = '29.06.2022'
        h_time = str('from 15.06.2022 to ' + date)

        # wybierz losowy typ wyżywienia
        if random.random() < 0.67:
            board_type = 'all-inclusive'
        else:
            board_type = 'śniadanie'

        h_board = board_type
        for hotel in hotels:
            hotel['time'] = str(date)
            hotel['days'] = str(days)
            hotel['board_type'] = str(board_type)


        for i in range(0,len(offers_a)):
            print('\nID: ' + str(i + 1) + '\nName: ' + sorted_hotels[i]['name'] + '\nCountry: ' + sorted_hotels[i][
                'country'] + '\nCategory: '
                               + sorted_hotels[i]['stars'] + ' stars' + '\nPrice per person: ' + str(
                sorted_hotels[i]['price']) + '\nTime frame: ' + h_time + '\nDays: ' + str(days)
                               + '\nBoard type: ' + h_board)



        return offers_a, date, h_board



    def checkout(offers):
        id = input("\nPlease enter an ID of the offer -> ")
        return offers[0][int(id)-1]





    def price_calc(offer):
        flight_price = 0

        adults = int(input("\nNumber of adults -> "))
        childern = int(input("\nNumber of childern -> "))
        hotel_price = (int(offer['price']) * adults * int(offer['days'])) + (int(offer['price']) * 1/2 * childern * int(offer['days']))

        match offer['country']:
            case "Grecja":
                flight_price = 1000
            case "Hiszpania":
                flight_price = 1000
            case "Egipt":
                flight_price = 1500
            case "Tajlandia":
                flight_price = 2000
            case "Meksyk":
                flight_price = 2500

        match offer['board_type']:
            case 'all-inclusive':
                board_price = 1200
            case 'śniadanie':
                board_price = 0
        final_price = flight_price + hotel_price + board_price
        print("Cena finalna: " + str(final_price))



Trip.price_calc(Trip.checkout(Trip.offers(hotels)))


