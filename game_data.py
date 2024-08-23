game_steps = {
    1: {
        'scenario': 'Du vaknar upp i en glänta, desorienterad och ensam. En bultande smärta i ditt huvud är en ständig påminnelse om olyckan som förde dig hit. Ditt sista minne är att du satt i ett flygplan. När du ser dig omkring inser du att du är djupt inne i en tät skog. '
                    'Vad ska du göra nu?',
        'options': {
            'a': 'Sök igenom din närhet efter användbara föremål.',
            'b': 'Utforska omgivningen.',
        },
        'next': {
            'a': 2,
            'b': 3
        }
    },
    2: {
        'scenario': 'Du går runt i skogen. Brusandet av löv och knakande grenar bildar en symfoni runt dig.'
                    'I skogens mitt hittar du bärbuskar med små blå-svarta bär, din mage börja kurrar när du ser bären.',
        'options': {
            'a': 'Är du hungrig nog att chansa och äta bären direkt?',
            'b': 'Eller sparar du bären till senare i hopp om att du kan identifiera om de är säkra att äta?',
        },
        'next': {
            'a': 'gameover',
            'b': 3
        },
        'gameover': 'Du känner dig svimfärdig och tuppar av då det var ett giftigt bär du hittat, ett mycket giftig bär som liknar blåbär. Spelet är över.'
    },
    3: {
        'scenario': 'En bit bort skymtar du en sjö som du rör dig mot. Det är kyligt men det glittrande vattnet är vackert på ett behagligt sätt och du ser några '
                    'fiskar simma vid ytan.',
        'options': {
            'a': 'Försök att fånga en fisk med händerna.',
            'b': 'Följ en stig som leder bort från sjön.',
        },
        'next': {
            'a': 4,
            'b': 5
        }
    },
    4: {
        'scenario': 'Du lyckas fånga en liten fisk, men vattnet är kallt och du börjar frysa. '
                    'Du måste hitta ett sätt att torka och värma dig.',
        'options': {
            'a': 'Sök efter torra grenar och försök göra upp en eld.',
            'b': 'Fortsätt att utforska området i hopp om att hitta skydd.',
        },
        'next': {
            'a': 'gameover',
            'b': 'gameover'
        },
        'gameover': 'Du lyckas inte hitta ett skydd eller få igång någon elden innan det blir natt. Du fryser ihjäl. Spelet är över.'
    },
    5: {
        'scenario': 'Stigen leder dig till en gammal stuga. Stugan ser övergiven ut, '
                    'men det kan vara ett bra ställe att söka skydd.',
        'options': {
            'a': 'Gå in i stugan och undersök den.',
            'b': 'Fortsätt att utforska området runt stugan.',
        },
        'next': {
            'a': 6,
            'b': 8
        },
    },
    6: {        
        'scenario': 'Inuti stugan hittar du några gamla möbler och en kamin. Det finns också några konserverade matvaror, som enkelt går att öppna. mmh gott... ',
        'options': {
            'a': 'Utforska stugan mer noggrant för att se om det finns något användbart.',
            'b': 'Försök att göra upp en eld i kaminen.',
        },
        'next': {
            'a': 7,
            'b': 'gameover'
        },
        'gameover': 'Du lyckas få igång elden men missade att skorsten ej fungerade. Under natten fylls stugan med kolmonoxid och du dör. Spelet är över.'
    },
    7: {        
        'scenario': 'Du ser dig om kring och ser två dörrar. En leder till ett sovrum och den andra till ett förråd.'
                    '',
        'options': {
            'a': 'Du går in i sovrummet för att vila.',
            'b': 'Du går in i förrådet för att se om det finns något användbart.',
        },
        'next': {
            'a': 'gameover',
            'b': 'gamever'
        },
        'gameover': 'Du trampar på en gammal fälla som går av och skadar dig allvarligt. Du blöder ihjäl. Spelet är över, börja om från början.'
    },
    8: {        
        'scenario': 'Du hittar en liten trädgård bakom stugan med några grönsaker som fortfarande växer.',
        'options': {
            'a': 'Plocka några grönsaker för att äta.',
            'b': 'Fortsätt att utforska området för att hitta fler resurser.',
        },
        'next': {
            'a': 9,
            'b': 'gameover'
        },
        'gameover': 'En liten bit bort trampar på en gammal fälla som går av och skadar dig allvarligt. Du blöder ihjäl. Spelet är över, börja om från början.'
    },
    9: {        
        'scenario': 'Med lite mat i magen fortsätter du bort ifrån stugan'
                    'Du hittar en liten bäck med klart vatten som rinner ner från en kulle. Det ser ut att finnas minst en timmes dagsljus kvar.'
                    '',
        'options': {
            'a': 'Drick från bäcken, det är bäst du håller vätskebalansen uppe.',
            'b': 'Fortsätt framåt i hop om att du kan hitta en plats där du kan sova säkert under natten.',
        },
        'next': {
            'a': 'gameover',
            'b': 10
        },
        'gameover': 'Vattnet visar sig vara förorenat och du blir sjuk. Du dör av förgiftning. Spelet är över, börja om från början.'
    },
    10: {        
        'scenario': 'Du lyckas hitta en liten grotta lite längre bort från bäcken. Det ser ut som ett perfekt ställe att sova för natten.'
                    '',
        'options': {
            'a': 'Gå in i för att vila din trötta ben.',
            'b': 'Utanför grottan finns det lite torrt gräs och några pinnar, samla några innan du går till sömns för att göra upp en eld.',
        },
        'next': {
            'a': 'gameover',
            'b': 11,
        },
        'gameover': 'Under natten kommer en björn och du lyckas inte undkomma i tid. Du blir dödad av björnen. Spelet är över, börja om från början.'
    },
    11: {        
        'scenario': 'Du lyckas upprätthålla en behaglig temperatur och vaknar nästa morgon, utvilad och redo att fortsätta ditt äventyr'
                    'Morgonen är här, du vaknar och njuter av solstrålarna som letar sig in i grottan. Du är hungrig och törstig, men du känner dig säker för tillfället.',
        'options': {
            'a': 'Försöka hitta något att äta och drick.',
            'b': 'Utforska grottan mer noggrant.',
        },
        'next': {
            'a': 12,
            'b': 'gameover'
        },
        'gameover': 'Du råkar stöta på en giftig orm och blir biten. Du dör av giftet. Spelet är över, börja om från början.'
    },
    12: {        
        'scenario': 'Du reser dig upp och går ut ur grottan. Du känner dig stark och redo att fortsätta din resa.'
                    'Efter att ha promenerat en stund ser du en skylt som pekar mot Vänneböke',
        'options': {
            'a': 'Försök hitta mat och vatten för resan.',
            'b': 'Påbörja resan mot Vänneböke by.',
        },
        'next': {
            'a': 13,
            'b': 'gameover'
        },
        'gameover': 'Du vandrar genom skogen i timmar utan att hita varken mat eller vatten. Du blir uttorkad och svag. Du dör av vätskebrist. Spelet är över, börja om från början.'
    },
    13: {        
        'scenario': 'Du hittar några björnbär och dricker lite mer vatten från bäcken. Du är redo att på börja din resa.'
                    'Du vandrar genom skogen och plötsligt ser du något mellan träden. Du går närmare, och du ser att det är en fyrhjuling. Någon har lämnat den där, övergiven och täckt med löv.',
        'options': {
            'a': 'Loota fyrhjulingen för användbara delar.',
            'b': 'Försök starta fyrhjulingen för att ta dig till Vänneböke snabbare.',
        },
        'next': {
            'a': 'gameover',
            'b': 14
        },
        'gameover': 'Du tömmer fyrhjulingen på bränsle och tar med dig några nödvändiga delar, men när du återvänder till stigen möts du av en björn. Du försöker att fly men trillar och skadar din fot svårt. Du blir uppäten av björnen. Spelet är över, börja om från början.'
    },
    14: {        
        'scenario': 'Trots att den är gammal, lyckas du starta den. Resan till Vänneböke ser ut att bli mycket enklare nu.',
        'options': {
            'a': 'Följ skylten du såg tidigare mot Vänneböke.',
            'b': 'Utforska omgivningen med fyrhjulingen för att hitta fler resurser.',
        },
        'next': {
            'a': 15,
            'b': 'gameover'
        },
        'gameover': 'Du kör runt i skogen, men plötsligt blir du attackerad av en vargflock. De attackerar dig och du dör. Spelet är över, börja om från början.'
    },
    15: {        
        'scenario': 'Du kör fyrhjulingen längs den trånga stigen i skogen och när dagsljuset börjar ta slut har Vänneböke äntligen kommit inom synhåll'
                    'När du närmar dig byn märker du att det är tyst och öde, men du fortsätter in i Vänneböke och kommer till en tom yta med ett ensamt hus i mitten. Du ser en skylt, \"Vänneböke 2279\". Det här är platsen du letat efter, du kan knappt tro att du äntligen hittat den.',
        'options': {
            'a': 'Se om ytterdörren är låst',
            'b': 'Undersök området mer noggrant först.',
        },
        'next': {
            'a': 'gameover',
            'b': 16
        },
        'gameover': 'Du trycker ner dörrhandtaget och kliver in i huset. Det är mörkt och tyst inne, du kan knappt se något. När du går framåt skymtar du en skugga några meter fram. Plötsligt, en dundrande smäll - personen i huset har uppfattat dig som ett hot och skjuter dig med ett hagelgevär. Du faller till golvet, allt blir svart. Spelet är över, börja om från början.'
    },
    16: {        
        'scenario': 'Du undersöker området runt huset och säkerställer att det inte finns några dolda faror. När du känner att du gjort allt du kan för att säkra platsen går du mot huset och kliver upp för trappan',
        'options': {
            'a': 'Knacka på dörren',
            'b': 'öppna dörren och gå in',
        },
        'next': {
            'a': 17,
            'b': 'gameover'
        },
        'gameover': 'Du trycker ner dörrhandtaget och kliver in i huset. Det är mörkt och tyst inne, du kan knappt se något. När du går framåt skymtar du en skugga några meter fram. Plötsligt, en dundrande smäll - personen i huset har uppfattat dig som ett hot och skjuter dig med ett hagelgevär. Du faller till golvet, allt blir svart. Spelet är över, börja om från början.'
    }, 
    17: {        
        'scenario': 'Du hör ljud innefrån huset, det låter som att någon lägger ifrån sig en bok och närmar sig dörren',
        'completed': True
    },           
}