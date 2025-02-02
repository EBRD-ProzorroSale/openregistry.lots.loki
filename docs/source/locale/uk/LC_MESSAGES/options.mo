��          T               �   �  �   ,   Y     �  �   �  )  �  �   �  �  9  �    d   �	  
   :
  �  E
       �   5   In addition to providing fields and their values in a request, you may also specify options to control how your request is interpreted and how the response is generated.  For GET requests, options are specified as URL parameters prefixed with `opt_`.  For POST or PUT requests, options are specified in the body, inside the top-level options object (a sibling of the data object).  The option specified in the body overrides the `opt_` one from URL parameter. List of extra fields to include in response. Options Provides the response in "pretty" output.  In case of JSON this means doing proper line breaking and indentation to make it readable.  This will take extra time and increase the response size so it is advisable to use this only during debugging. Returns the output in JSON-P format instead of plain JSON. This allows requests to come from within browsers and work around the "same origin policy." The function named as the value of the `opt_jsonp` parameter will be called with a single argument, a JavaScript object representing the response. These options can be used in different combinations in a single request, though some of them may conflict in their impact on the response. Project-Id-Version: openregistry.lots.basic 0.1.dev0
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2017-08-19 13:20+0300
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: uk
Language-Team: uk <LL@li.org>
Plural-Forms: nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.4.0
 Крім надання полів та їхніх значень у запиті ви можете ще вказати опції для контролю над тим, як буде оброблятись запит і як буде генеруватись відповідь. Для GET запитів, опції вказуються як URL параметри з префіксом `opt_`. Для POST чи PUT запитів опції вказуються в тілі, всередині об’єктів опцій вищого рівня (схожих на обє’кт даних). Опція вказана в тілі перевизначає `opt_` опцію з URL параметра. Список додаткових полів, що міститимуться у відповіді. Опції Надає відповідь у форматі “pretty”. У випадку з JSON це означає правильне розбиття рядків і відступи для зручності читання. Це займе додатковий час і збільшить розмір відповіді, тому краще буде використовувати цю опцію тільки під час налагоджування (debugging). Повертає відповідь у форматі JSON-P замість простого JSON, щоб дозволити запитам приходити з браузерів і працювати навколо “однакової політики походження (same origin policy).” Функція названа так само як значення параметра `opt_jsonp` буде викликана з одним аргументом - JavaScript об’єктом, що представляє відповідь. Ці опції можна комбінувати в одному запиті, хоча деякі з них можуть викликати конфлікт у відповіді. 