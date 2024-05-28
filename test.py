def process_people(people):
    results = []
    for person in people:
        if 'name' in person:
            name = person['name']
            if 'age' in person:
                age = person['age']
                if age > 18:
                    age_group = 'adult'
                else:
                    age_group = 'minor'
            else:
                age_group = 'unknown'
        else:
            name = 'unknown'
            age_group = 'unknown'
        
        if 'city' in person:
            city = person['city']
            if city == 'New York':
                city_group = 'NY'
            elif city == 'Los Angeles':
                city_group = 'LA'
            else:
                city_group = 'Other'
        else:
            city = 'unknown'
            city_group = 'unknown'
        
        for char in name:
            if char in 'AEIOUaeiou':
                vowel = True
            else:
                vowel = False
        
        if vowel:
            for i in range(len(name)):
                if i % 2 == 0:
                    if name[i].isupper():
                        char_type = 'uppercase'
                    else:
                        char_type = 'lowercase'
                else:
                    char_type = 'mixed'
        else:
            char_type = 'consonant'
        
        results.append({
            'name': name,
            'age_group': age_group,
            'city_group': city_group,
            'char_type': char_type
        })
    
    for result in results:
        if result['age_group'] == 'adult':
            if result['city_group'] == 'NY':
                result['status'] = 'NY Adult'
            elif result['city_group'] == 'LA':
                result['status'] = 'LA Adult'
            else:
                result['status'] = 'Other Adult'
        else:
            result['status'] = 'Minor or Unknown'
    
    final_results = []
    for result in results:
        if result['status'] == 'NY Adult':
            if result['char_type'] == 'uppercase':
                final_results.append(result)
            elif result['char_type'] == 'lowercase':
                final_results.append(result)
            else:
                pass
        else:
            if result['status'] == 'Minor or Unknown':
                final_results.append(result)
    
    return final_results
