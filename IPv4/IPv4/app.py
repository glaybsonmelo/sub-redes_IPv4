from classes.cls import CalcIPv4


def main():
    ip = input('IP: ')
    opc = input('Calcular com Prefixo ou Mascara?\n'
    '[1] Mascara\n'
    '[2] Prefixo\n'
    'Escolha a opção: ')
    if opc == '1':
        mascara = input('Mácara: ')
        prefixo = None
    elif opc == '2':
        prefixo = input('Prefixo: ')
        mascara = None
    else:
        print('Opção invalida!')

    calc_ipv4_1 = CalcIPv4(ip, mascara, prefixo)

    print(f'IP: {calc_ipv4_1.ip}')
    print(f'Máscara: {calc_ipv4_1.mascara}')
    print(f'Rede: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefixo: {calc_ipv4_1.prefixo}')
    print(f'Número de IPs da rede: {calc_ipv4_1.numero_ips}')


if __name__ == '__main__':
    main()