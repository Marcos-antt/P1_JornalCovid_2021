from flask import Flask
import os
from application.model.entity.categoria import Categoria
from application.model.entity.video import Video

template_folder = os.path.abspath('application/view/templates')
static_folder = os.path.abspath('application/view/static')

app = Flask(__name__,template_folder = template_folder, static_folder = static_folder)


video1 = Video(1,"RJ registra maior número de mortes por Covid em um mês desde o início da pandemia","Pesquisadores do Observatório COVID-19 BR acreditam que expansão de horários pode levar a maior risco de transmissão da Covid-19 no estado. Estabelecimentos comerciais poderão funcionar das 6h às 20h a partir deste sábado e foram recomendados a receber apenas 25% do público máximo; antes, horário era das 11h às 19h.",'img/img_categoria/noticia_2.jpg', 'rio_video.mp4' , 'O Estado do Rio registrou em abril deste ano o maior número de mortes causadas pela Covid em um mês desde o início da pandemia no país. Foram 6.788 óbitos causados pela doença até a tarde desta sexta-feira (30), segundo dados do Portal da Transparência do Registro Civil.' )
video2 = Video(2,"Especialistas criticam mudança na fase de transição da quarentena em SP, que permite ampliar horários a partir deste sábado","Em abril deste ano, o estado já registrou 6.788 óbitos causados pela doença, segundo dados do Portal da Transparência do Registro Civil. Até o momento, maio de 2020 era o mês com maior mortes relacionadas à Covid.",'img/img_categoria/noticia_1.jpg','sp_video.mp4', 'O governo de São Paulo ampliou o horário de funcionamento de lojas, shoppings, restaurantes, salões de beleza, academias e outros estabelecimentos comerciais, que a partir deste sábado (1º) poderão funcionar das 6h às 20h, o equivalente a 14 horas diárias. Antes da mudança, a fase de transição permitia o funcionamento apenas por 8h diárias, das 11h às 19h, para a maior parte dos setores (veja na tabela abaixo o que muda). Segundo oito pesquisadores ouvidos pelo G1, a expansão de horários pode levar a maior risco de transmissão da Covid-19 no estado. ENTENDA: as fases do plano São Paulo MORTES EM SP: estado ultrapassa 90 mil óbitos por Covid-19 MORTALIDADE: óbitos em SP equivalem a 32% do número de pacientes que tiveram alta Membros do Observatório COVID-19 BR dizem que a mudança traz preocupação porque a flexibilização das regras foi baseada principalmente na queda da taxa de ocupação dos leitos de UTI, considerado “um indicador fraco e tardio da evolução da pandemia, segundo a própria Organização Mundial da Saúde (OMS)”')


video_list = [video1, video2]

categoria_list = []
categoria1 = Categoria(1,"Rio de Janeiro - RJ","Acompanhe as notcias do Estado do Rio de Janeiro",'img/img_categoria/rio_de_janeiro.png',[video1])
categoria2 = Categoria(2,"São Paulo - SP","Acompanhe as notcias do Estado de São Paulo",'img/img_categoria/sao_paulo.png',[video2])

categoria_list = [categoria1,categoria2]

from application.controller import index_controller
from application.controller import video_controller

