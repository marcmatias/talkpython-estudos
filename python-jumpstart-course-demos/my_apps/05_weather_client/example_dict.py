def main():
    d = {
            'city': 'Portland',
            'state': 'ME',
            'country': 'DE',
            'details': ['Cold', 'Snowy', 'Winter'],
    }

    # print(d)
    # print(d['city'])
    print(d.get('country', 'USA'))
    d['country'] = 'AU'
    print(d.get('country', 'USA'))
    print(d)

if __name__ == '__main__':
    main()
