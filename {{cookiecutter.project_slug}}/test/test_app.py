def test_nothing():
    assert True

def test_import():
    import {{cookiecutter.package_name}}
    from {{cookiecutter.package_name}} import cli
    cli.main()
