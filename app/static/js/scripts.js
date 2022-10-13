function simple_passgen(alphabet, length){
    if(window.crypto && window.crypto.getRandomValues) {
		return Array(length)
			.fill(alphabet)
			.map(x => x[Math.floor(crypto.getRandomValues(new Uint32Array(1))[0] / (0xffffffff + 1) * x.length )])
			.join('');    
	} 
    else {
		let pass = "";
		for (let i = 0, n = alphabet.length; i < length; ++i) {
			pass += alphabet.charAt(Math.floor(Math.random() * n));
		}
		return pass;
	}
}

$(document).on('click', '#simplepass-gen-btn', function(ev){
    let symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
    let russian = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя";
    let english = "abcdefghijklmnopqrstuvwxyz";
    let numbers = "0123456789";
    charset_hashset = {
        "symbols": symbols,
        "russian_lower":russian.toLowerCase(),
        "russian_upper":russian.toUpperCase(),
        "english_lower":english.toLowerCase(),
        "english_upper":english.toUpperCase(),
        "numbers":numbers,
    }
    let length = parseInt($("#pass_length").val());
    let alphabet = "";
    let charsets = $("input.form-check-input:checked");
    if (!charsets.length){
        $("#pass-out-field").text("Выберите хотя бы один набор значенний для алфавита");
    }
    else {
        for (let el of charsets){
            alphabet += charset_hashset[el.value];
        };
        let password = simple_passgen(alphabet, length);
        $("#pass-out-field").text(password);
    }
})


function passphrase_passgen(phrase, char_number){
    let russ_chars = 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'.split('');
    let eng_chars = '`qwertyuiop[]asdfghjkl;\'zxcvbnm,.~QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>'.split('');
    let сhars_mapper = {}
    russ_chars.forEach((n, index) => сhars_mapper[n] = eng_chars[index]);

    let pass = phrase
        .split(' ')
        .map(x => x.substr(0, char_number))
        .map(x => x.split('').map(x => сhars_mapper[x]).join(''))
        .join('');

    return pass
}

$(document).on('click', '#passphrase-gen-btn', function(ev){
    let char_number = parseInt($("#char_number").val());
    let phrase = $("#phrase-out-field").val().trim();

    if (!phrase.length){
        $("#pass-out-field").text("Введите парольную фразу");
    }
    else {
        let password = passphrase_passgen(phrase, char_number);
        $("#pass-out-field").text(password);
    }
})

$(document).on('click', '#phrase-gen-btn', function(ev){
    let word_number = parseInt($("#phrase_length").val());
    $.get(document.location.href + "/api/"+ word_number, function(data){
        let phrase = data['phrase'];
        $("#phrase-out-field").val(phrase);
    }, 'json');
})