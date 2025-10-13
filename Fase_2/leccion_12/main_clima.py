from api_clima import obtener_clima, obtener_ubicacion_actual, obtener_clima_por_coordenada

if __name__ == "__main__":
    while True:
        print("\n--- MENÚ ---")
        print("1. Consultar clima por ciudad (CDMX, Monterrey, Guadalajara)")
        print("2. Consultar clima de tu ubicación actual")
        print("3. Consultar clima por coordenadas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ciudad = input("Ciudad: ")
            temp = obtener_clima(ciudad)
            if temp is not None:
                print(f"🌡️ La temperatura en {ciudad} es {temp}°C")

        elif opcion == "2":
            ciudad, lat, lon = obtener_ubicacion_actual()
            if ciudad:
                print(f"📍 Tu ubicación detectada: {ciudad["city"]} ({lat}, {lon})")
                temp = obtener_clima(ciudad, lat, lon)
                if temp is not None:
                    print(f"🌡️ La temperatura actual en {ciudad} es {temp}°C")

        elif opcion == "3":
            lat, lon = obtener_clima_por_coordenada()
            temp = obtener_clima("",lat,lon)
            if temp is not None:
                print(f"La temperatura actual en latitud:{lat}, longitud{lon} es: {temp}°C") 

        elif opcion == "4":
            print("👋 Saliendo...")
            break

        else:
            print("⚠️ Opción inválida.")
