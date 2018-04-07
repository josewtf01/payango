import flask
import shutil , os
import qrcode
import qr_gen_test
import documents_test

#paypal - 1
link = "PayPal.Me/jos17ing"
name_file = "paypal.png"
qr_gen_test.make_qr(link,name_file)
# os.chdir('F:\\talent_land_2018\\payango\\email')
# print(os.getcwd())
#shutil.copy('F:\\talent_land_2018\\payango\\flask\\' + str(name_file),
#'F:\\talent_land_2018\\payango\\email')

#bitso - 2
link = "https://bitso.com/"
name_file = "bitso.png"
qr_gen_test.make_qr(link,name_file)
#shutil.copy('F:\\talent_land_2018\\payango\\flask\\' + str(name_file),
#'F:\\talent_land_2018\\payango\\email')

#mercado pago -3
link = "https://www.mercadopago.com.mx/como-cobrar#herramienta-todo-resuelto"
name_file = "mercado.png"
qr_gen_test.make_qr(link,name_file)
#shutil.copy('F:\\talent_land_2018\\payango\\flask\\' + str(name_file),
#'F:\\talent_land_2018\\payango\\email')

# banamex -4
link = "https://www.banamex.com/"
name_file = "banamex.png"
qr_gen_test.make_qr(link,name_file)
#shutil.copy('F:\\talent_land_2018\\payango\\flask\\' + str(name_file),
#'F:\\talent_land_2018\\payango\\email')

# conekta -5
link = "https://www.conekta.com/es/oxxopay?ref=nav"
name_file = "conekta.png"
qr_gen_test.make_qr(link,name_file)
#shutil.copy('F:\\talent_land_2018\\payango\\flask\\' + str(name_file),
#'F:\\talent_land_2018\\payango\\email')

# payulatam -6
link = "https://tether.to/"
name_file = "tether.png"
qr_gen_test.make_qr(link,name_file)
#shutil.copy('F:\\talent_land_2018\\payango\\flask\\' + str(name_file),
#'F:\\talent_land_2018\\payango\\email')

# docto = documents_test.official_document()
# print(docto.show_curp())
