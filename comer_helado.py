apetece_helado_input = input("¿Te apetece un helado? (Si / No):").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetec_helado = False
else:
    print("Te he dicho que me digas SI o NO, nose que has dicho pero cuenta como que NO")
    apetec_helado = False

tiene_dinero_input = input("¿Tienes dinero para el helado? (Si / No)").upper()

if tiene_dinero_input == "SI":
    tiene_dinero = True
elif tiene_dinero_input == "NO":
    tiene_dinero = False
else:
    print("Te he dicho que me digas SI o NO, nose que has dicho pero cuenta como que NO")
    apetec_helado = False

esta_el_seno_helados_input = input("¿Esta el señor de los helados? (Si / No)").upper()

if esta_el_seno_helados_input == "SI":
    esta_el_seno_helados = True
elif esta_el_seno_helados_input == "NO":
    esta_el_seno_helados = False
else:
    print("Te he dicho que me digas SI o NO, nose que has dicho pero cuenta como que NO")
    apetec_helado = False

esta_su_tia_input = input("¿Estas con tu tia?").upper()

apetece_helado = apetece_helado_input == "SI"
tiene_dinero = tiene_dinero_input == "SI"
esta_su_tia = esta_su_tia_input == "SI"
puede_permitirselo = tiene_dinero or esta_su_tia
esta_el_senor_helados = esta_el_seno_helados_input == "SI"



if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Pues comete un helado")

else:
    print("Pues nada tu te lo pierdes")

