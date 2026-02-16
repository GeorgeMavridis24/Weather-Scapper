import requests








def get_weather_data(city_name):
  
  

    url =  f"https://wttr.in/{city_name}?format=j1"
    print(f"Συνδέομαι στο wttr.in για {city_name}...")

    try:
        response = requests.get(url)
      
        data = response.json()
        current_condition = data['current_condition'][0]
        temp = current_condition['temp_C']
        desc =current_condition['weatherDesc'][0]['value'] 
        return temp, desc

    except Exception as ex:
        print(f"Σφάλμα σύνδεσης: {ex}")
        return None, None




if __name__ == "__main__":
    user_city = input("Για ποια πόλη θες να μαθεις; (Γράψε π.χ. Athens): ")
    
   
    temp,desc = get_weather_data(user_city)

    
    if temp:
        print(f"Η τρέχουσα θερμοκρασία στην {user_city} είναι {temp}°C και ο καιρος είναι {desc}.")
    else:
        print("Δεν μπόρεσα να πάρω τα δεδομένα καιρού.")


input("\nΠάτα ENTER για να κλείσει το πρόγραμμα...")
        