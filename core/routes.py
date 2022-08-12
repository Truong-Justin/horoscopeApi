from core import api
from flask import jsonify
from core.utils import getHoroscopeByDay, getHoroscopeByWeek, getHoroscopeByMonth, getChineseHoroscopeByDay, getChineseHoroscopeByWeek, getChineseHoroscopeByMonth
from flask_restx import Resource, reqparse
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime



api = api.namespace('/', description='Horoscope APIs')


ZODIAC_SIGNS = {
    "Aries": 1,
    "Taurus": 2,
    "Gemini": 3,
    "Cancer": 4,
    "Leo": 5,
    "Virgo": 6,
    "Libra": 7,
    "Scorpio": 8,
    "Sagittarius": 9,
    "Capricorn": 10,
    "Aquarius": 11,
    "Pisces": 12
}

chineseZodiac = {
    "Ox": 1,
    "Goat": 2,
    "Rat": 3,
    "Snake": 4,
    "Dragon": 5,
    "Tiger": 6,
    "Rabbit": 7,
    "Horse": 8,
    "Monkey": 9,
    "Rooster": 10,
    "Dog": 11,
    "Pig": 12
}


parser = reqparse.RequestParser()
parser.add_argument("sign", type=str, required=True)
parser_copy = parser.copy()
parser_copy.add_argument("day", type=str, required=True,
                         help="Accepted values: Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY")


chineseZodiacParser = reqparse.RequestParser()
chineseZodiacParser.add_argument("animal", type=str, required=True)
chineseZodiacParserCopy = chineseZodiacParser.copy()
chineseZodiacParserCopy.add_argument("day", type=str, required=True,
                                    help="Accepted values: Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY")



#Returns daily horoscope when /get-horoscope/daily endpoint is accessed
@api.route("/get-horoscope/daily")
class DailyHoroscopeAPI(Resource):
    @api.doc(parser=parser_copy)
    
    def get(self):
        args = parser_copy.parse_args()
        day = args.get('day')
        zodiac_sign = args.get('sign')
        
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            horoscope_data = getHoroscopeByDay(zodiac_num, day)
            return jsonify(success=True, data=horoscope_data, status=200)
        
        except KeyError:
            raise NotFound('No such zodiac sign exists')
        
        except AttributeError:
            raise BadRequest(
                'Something went wrong, please check the URL and the arguments.')
        
        except ValueError:
            raise BadRequest('Please enter day in correct format: YYYY-MM-DD')


#returns weekly horoscope when /get-horoscope/weekly endpoint is accessed
@api.route("/get-horoscope/weekly")
class WeeklyHoroscopeAPI(Resource):
    @api.doc(parser=parser)
    
    def get(self):
        args = parser.parse_args()
        zodiac_sign = args.get('sign')
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            horoscope_data = getHoroscopeByWeek(zodiac_num)
            return jsonify(success=True, data=horoscope_data, status=200)
        
        except KeyError:
            raise NotFound('No such zodiac sign exists')
        
        except AttributeError:
            raise BadRequest(
                'Something went wrong, please check the URL and the arguments.')


#returns monthly horoscope when /get-horoscope/monthly endpoint is accessed
@api.route("/get-horoscope/monthly")
class MonthlyHoroscopeAPI(Resource):
    @api.doc(parser=parser)
    
    def get(self):
        args = parser.parse_args()
        zodiac_sign = args.get('sign')
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            horoscope_data = getHoroscopeByMonth(zodiac_num)
            return jsonify(success=True, data=horoscope_data, status=200)
        
        except KeyError:
            raise NotFound('No such zodiac sign exists')
        
        except AttributeError:
            raise BadRequest(
                'Something went wrong, please check the URL and the arguments.')


#returns daily chinese horoscope when /get-chineseHoroscope/daily
@api.route("/get-chineseHoroscope/daily")
class DailyChineseHoroscope(Resource):
    @api.doc(parser=chineseZodiacParserCopy)
    
    def get(self):
        args = chineseZodiacParserCopy.parse_args()
        day = args.get('day')
        zodiacAnimal = args.get('animal')
        try:
            chineseZodiacNum = chineseZodiac[zodiacAnimal.capitalize()]
            horoscope_data = getChineseHoroscopeByDay(chineseZodiacNum, day)
            return jsonify(success=True, data = horoscope_data, status=200)
        
        except KeyError:
            raise NotFound("Sign not found")
        
        except AttributeError:
            raise BadRequest("Something went wrong, please check the URL and arguments.")
        
        except ValueError:
            raise BadRequest("Please enter day in correct format: YYYY-MM-DD")


#returns daily chinese horoscope when /get-chineseHoroscope/weekly
@api.route("/get-chineseHoroscope/weekly")
class WeeklyChineseHoroscope(Resource):
    @api.doc(parser = chineseZodiacParser)
    
    def get(self):
        args = chineseZodiacParser.parse_args()
        zodiacAnimal = args.get("animal")
        try:
            chineseZodiacNum = chineseZodiac[zodiacAnimal.capitalize()]
            horoscopeData = getChineseHoroscopeByWeek(chineseZodiacNum)
            return jsonify(success=True, data = horoscopeData, status=200)

        except KeyError:
            raise NotFound("Sign not found")
        
        except AttributeError:
            raise BadRequest("Something went wrong, please check the URL and arguments.")
        
        except ValueError:
            raise BadRequest("Please enter day in correct format: YYYY-MM-DD")


#returns daily chinese horoscope when /get-chineseHoroscope/monthly
@api.route("/get-chineseHoroscope/monthly")
class MonthlyChineseHoroscope(Resource):
    @api.doc(parser = chineseZodiacParser)
    
    def get(self):
        args = chineseZodiacParser.parse_args()
        zodiacAnimal = args.get("animal")
        try:
            chineseZodiacNum = chineseZodiac[zodiacAnimal.capitalize()]
            horoscopeData = getChineseHoroscopeByMonth(chineseZodiacNum)
            return jsonify(success=True, data = horoscopeData, status=200)

        except KeyError:
            raise NotFound("No such animal exists")

        except AttributeError:
            raise BadRequest("Something went wrong, please check the URL and arugments")
                
