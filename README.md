# Discord-Time-Stamp-Bot
Darbs veidots sadarbībā starp Raivo Rosvaldu un Renāru Garderu
## Projekta uzdevums
Uzdevums: Izveidot programmatūru, kas discord serveros spēj ērti izveidot laika rādītājus('timestamps'). Timestamps ir funkcija sociālo tīklu vidē discord, kas no epoch laika (utc laiks kopš 1970. gada) pārveido to laikā, kompensējot laika zonām. Diemžēl discord vidē šos timestamps izveidot ir ļoti neērti, un ir nepieciešama mājaslapa lai noskaidrotu epoch laiku. Eksistē mājaslapa, no kuras man šī ideja radās https://r.3v.fi/discord-timestamps/, tomēr integrējot šo darbību discord servera botā, darbība tiek atvieglota un automatizēta.
Discord robotā pievienotas papildus funkcija: atsūtīt nejauši izvēlētu dzīvnieka bildi no konkrētas mājaslapas.

## Python bibliotēkas
nextcord - bibliotēka paredzēta komunikācijai starp python un discord api. Atzarojums no discordpy.
nextcord commands - bibliotēka paredzēta discord komandu izsaukšanai
nextcord interaction - Bibliotēka paredzēta saziņai starp discord botu un personu, kas izsauc komandu.
nextcord slashoption - bibliotēka paredzēta vairāku noteiktu izvēļu padošanā. Izmantots lai noteiktu laika pasniegšanas veidu.
datetime - bibliotēka paredzēta pašreizējā laika iegūšanai.
requests - pieprasa informāciju no attiecīgas mājaslapas (dzīvnieku bilžu ieguvei)
calendar - bibliotēka paredzēta lai pārveidotu laiku no parastā formāta uz epoch discord timestamp

## Programmatūras izmantošanas metodes
ar pip install pievienot sekojošās bibliotēkas:
nextcord
requests

discord developer portālā jāizveido savs bots, tam jādod atļaujas, jāpievieno serverim, kodā jāievieto komandās servera id.

Botam ir sekojošās komandas:
/epoch
komanda piedāvās laika attēlošanas formātus, šī ir vienīgā obligātā izvēle. Komandai var padot gadu, mēnesi, datumu, stundas, minūtes, sekundes, tomēr neviens nav obligāts. Ja vērtību nepadod, tiek padota pašreizējā laika vērtība (t.i. pašreizējā stunda, gads, minūte, u.t.t.) Komanda atgriezīs unix laiku discord timestamp formātā.

/fox
atgriezīs nejauši izvēlētu attēlu ar lapsu

/cat
atgriezīs nejauši izvēlētu attēlu ar kaķi

/dog
atgriezīs nejauši izvēlētu attēlu ar shibe-inu suni.

/bird
atgriezīs nejauši izvēlētu attēlu ar putnu.

/hello
bots ar tevi privāti sasveicināsies.
