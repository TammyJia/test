describe('add todo', function () {
    let page;

    before (async function () {
      page = await browser.newPage();
      await page.goto('http://127.0.0.1:3000/');
    });
  
    after (async function () {
      await page.close();
    });

    it('should have correct title', async function() {
        expect(await page.title()).to.eql('React App');
    })
    it('should new todo correct', async function() {
        // 点击输入框
      await page.click('#newcontent', {delay: 500});
      // 输入add todo事项
      await page.type('#newcontent', 'new todo item', {delay: 50});
      // 回车
      // await page.keyboard.press("Enter");
      await page.click('button', {delay: 50});
      // 断言，看实际的结果和我预估的结果是否相同，如果相同，则通过测试
      let todoList = await page.waitFor('#todo-list');
      const expectInputContent = await page.evaluate(todoList => todoList.lastChild.querySelector('label').textContent, todoList);
      expect(expectInputContent).to.eql('new todo item');
    }) 

  });

describe('list', function () {
    let page;

    before (async function () {
      page = await browser.newPage();
      await page.goto('http://127.0.0.1:3000/');
    });

    after (async function () {
      await page.close();
    });

    it('list number correct', async function() {
      const number = await page.evaluate(() => {
          return document.getElementsByTagName('li').length;
      });
      expect(number).to.eql(2);
    })

  });

describe('change state', function () {
    let page;

    before (async function () {
      page = await browser.newPage();
      await page.goto('http://127.0.0.1:3000/');
    });

    after (async function () {
      await page.close();
    });

    it('change todo list correct', async function() {
      await page.click("li[class='not-done']", {delay: 500});

      const number = await page.evaluate(() => {
          return document.getElementsByTagName('li[class=\'not-done\']').length;
      });
      expect(number).to.eql(0);
    })

  });