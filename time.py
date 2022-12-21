#variables
arbetsTid = 0

arbetsDagar = 0

#functions
def calculate_time (x, y): 
    return x - y

def add_time(x, y): 
    return x + y 

def average_time(x,y):
    return x // y

def average_days(x,y):
    return round((x / y),2)
    
#print
print("Din arbetstid för....")

veckoTimmar = calculate_time((17.5 + 18.0 + 17.0), (7.25 + 8.75 + 8.0))
print("  -vecka 45 är:", veckoTimmar, "timmar")
arbetsTid = add_time(arbetsTid, veckoTimmar)
arbetsDagar = arbetsDagar + 3

veckoTimmar = calculate_time((17.5 + 15.5 + 18.0 + 17.25 + 17.25), (7.25 + 6.75 + 8.75 + 7.75 + 7.75))
print("  -vecka 46 är:", veckoTimmar, "timmar")
arbetsTid = add_time(arbetsTid, veckoTimmar)
arbetsDagar = arbetsDagar + 5


veckoTimmar = calculate_time((18.0 + 17.0 + 18.0 + 17.0), (8.0 + 7.25 + 8.75 + 7.25))
print("  -vecka 47 är:", veckoTimmar, "timmar")
arbetsTid = add_time(arbetsTid, veckoTimmar)
arbetsDagar = arbetsDagar + 4

veckoTimmar = calculate_time((15.5 + 18.0 + 17.5 + 15.5 + 18.0), (6.75 + 8.0 + 7.25 + 6.75 + 8.0))
print("  -vecka 48 är:", veckoTimmar, "timmar")
arbetsTid = add_time(arbetsTid, veckoTimmar)
arbetsDagar = arbetsDagar + 5

veckoTimmar = calculate_time((18.0 + 17.0 + 17.5 + 17.25 + 18.0), (8.75 + 8.0 + 7.25 + 6.75 + 8.75))
print("  -vecka 49 är:", veckoTimmar, "timmar")
arbetsTid = add_time(arbetsTid, veckoTimmar)
arbetsDagar = arbetsDagar + 5

veckoTimmar = calculate_time((18.0 + 17.0 +17.5 + 15.5), (8.75 + 8.0 + 7.25 + 6.75))
print("  -vecka 50 är:", veckoTimmar, "timmar")
arbetsTid = add_time(arbetsTid, veckoTimmar)
arbetsDagar = arbetsDagar + 4

veckoTimmar = calculate_time((17.0 + 17.0 + 15.5), (8.0 + 7.25 + 6.75))
print("  -vecka 51 är:", veckoTimmar, "timmar")
arbetsTid = add_time(arbetsTid, veckoTimmar)
arbetsDagar = arbetsDagar + 3

veckoTimmar = calculate_time((16.5 + 18.0 + 17.0 + 17.0 + 17.25 + 17.25), (8.0 + 8.0 + 7.25 + 8.0 + 7.25 + 7.75))
print("  -vecka 52 är:", veckoTimmar, "timmar")
arbetsTid = add_time(arbetsTid, veckoTimmar)
arbetsDagar = arbetsDagar + 6

veckoTimmar = calculate_time((17.0 + 18.0 + 16.5 + 17.25 + 17.25), (7.25 + 8.0 + 8.0 + 7.75 + 7.75))
print("  -vecka 1 är:", veckoTimmar, "timmar")
arbetsTid = add_time(arbetsTid, veckoTimmar)
arbetsDagar = arbetsDagar + 5


print("\nDin totala arbetstid är:", arbetsTid, "timmar")

print("\nGenomsnittliga arbetstiden per vecka är ca:", average_time(arbetsTid, 9), "timmar")

print("\nTotala antalet dagar under 9 veckor är:", arbetsDagar)

print("\nGenomsnittligt antal dagar per vecka är:", average_days(arbetsDagar, 9))
